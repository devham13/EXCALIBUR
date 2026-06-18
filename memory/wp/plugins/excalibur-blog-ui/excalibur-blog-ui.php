<?php
/**
 * Plugin Name: Excalibur Blog UI
 * Description: AI Dev Editorial Interface — оформление технических статей блога.
 * Version: 2.1.0
 * Author: Excalibur BLOG
 * Text Domain: excalibur-blog-ui
 */

declare(strict_types=1);

if (!defined('ABSPATH')) {
    exit;
}

define('EBU_VERSION', '2.1.0');
define('EBU_FILE', __FILE__);
define('EBU_DIR', plugin_dir_path(__FILE__));
define('EBU_URL', plugin_dir_url(__FILE__));

final class Excalibur_Blog_UI
{
    public static function init(): void
    {
        add_action('wp_enqueue_scripts', [self::class, 'enqueue_assets']);
        add_filter('body_class', [self::class, 'body_class'], 99);
        add_action('wp_body_open', [self::class, 'render_reading_progress'], 4);
        add_action('wp_body_open', [self::class, 'render_floating_header'], 12);
        add_action('wp_head', [self::class, 'render_schema_jsonld'], 25);
        add_filter('kadence_post_layout', [self::class, 'hide_kadence_footer_blocks']);
        add_filter('theme_mod_post_related', [self::class, 'disable_kadence_related']);
        add_filter('theme_mod_post_navigation', [self::class, 'disable_kadence_navigation']);
        add_action('kadence_single_before_entry_header', [self::class, 'render_category_pill'], 6);
        add_filter('the_content', [self::class, 'enhance_faq_markup'], 30);
        add_action('kadence_single_before_entry_content', [self::class, 'open_article_stage'], 2);
        add_action('kadence_single_after_entry_content', [self::class, 'close_article_stage'], 100);
        add_action('kadence_single_after_content', [self::class, 'render_article_footer'], 8);
    }

    public static function is_blog_article(): bool
    {
        return is_singular('post');
    }

    public static function body_class(array $classes): array
    {
        if (!self::is_blog_article()) {
            return $classes;
        }

        $classes[] = 'excalibur-blog-single';
        $classes[] = 'nero-ai-landing';
        $classes = array_values(array_diff($classes, [
            'content-width-narrow',
            'content-style-boxed',
        ]));
        $classes[] = 'content-width-normal';
        $classes[] = 'content-style-unboxed';

        if (get_post_meta(get_queried_object_id(), '_excalibur_blog_skip_theme_faq', true) === '1') {
            $classes[] = 'excalibur-blog-article';
        }

        return $classes;
    }

    public static function enqueue_assets(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        wp_enqueue_style(
            'excalibur-blog-ui-fonts',
            'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Manrope:wght@600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap',
            [],
            null
        );

        $theme_dir = get_stylesheet_directory();
        $theme_uri = get_stylesheet_directory_uri();

        $layout_css = $theme_dir . '/longread-page-kadence-layout.css';
        if (is_readable($layout_css)) {
            wp_enqueue_style(
                'excalibur-blog-kadence-layout',
                $theme_uri . '/longread-page-kadence-layout.css',
                [],
                (string) filemtime($layout_css)
            );
        }

        $header_css = $theme_dir . '/nero-ai-floating-header.css';
        if (is_readable($header_css)) {
            wp_enqueue_style(
                'excalibur-blog-floating-header',
                $theme_uri . '/nero-ai-floating-header.css',
                [],
                (string) filemtime($header_css)
            );
        }

        wp_enqueue_style(
            'excalibur-blog-ui',
            EBU_URL . 'assets/blog-single.css',
            ['excalibur-blog-ui-fonts'],
            EBU_VERSION
        );

        $header_js = $theme_dir . '/nero-ai-floating-header.js';
        if (is_readable($header_js)) {
            wp_enqueue_script(
                'excalibur-blog-floating-header',
                $theme_uri . '/nero-ai-floating-header.js',
                [],
                (string) filemtime($header_js),
                true
            );
        }

        wp_enqueue_script(
            'excalibur-blog-ui',
            EBU_URL . 'assets/blog-single.js',
            [],
            EBU_VERSION,
            true
        );

        wp_localize_script('excalibur-blog-ui', 'ebuArticle', [
            'category'    => self::primary_category_label(),
            'readingTime' => self::reading_time_label(),
        ]);
    }

    public static function hide_kadence_footer_blocks(array $layout): array
    {
        if (!self::is_blog_article()) {
            return $layout;
        }

        $layout['navigation'] = 'hide';

        return $layout;
    }

    public static function disable_kadence_related($value)
    {
        if (self::is_blog_article()) {
            return false;
        }

        return $value;
    }

    public static function disable_kadence_navigation($value)
    {
        if (self::is_blog_article()) {
            return false;
        }

        return $value;
    }

    public static function render_reading_progress(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        echo '<div class="reading-progress" aria-hidden="true"><span data-reading-progress-fill></span></div>';
    }

    public static function render_floating_header(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        $inc = get_stylesheet_directory() . '/nero-ai-floating-header.inc.php';
        if (!is_readable($inc)) {
            return;
        }

        $brand = get_bloginfo('name') ?: 'Neurinix';
        $primary_cta_label = self::cta_label('primary');
        $primary_cta_url = self::cta_url('primary');
        $secondary_cta_label = self::cta_label('secondary');
        $secondary_cta_url = self::cta_url('secondary');

        $nero_ai_header_links = [
            ['label' => 'Главная', 'href' => home_url('/')],
            ['label' => 'Содержание', 'href' => '#article-toc'],
            ['label' => 'FAQ', 'href' => '#faq'],
        ];

        include $inc;
    }

    public static function render_schema_jsonld(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        $schema = get_post_meta(get_queried_object_id(), '_excalibur_blog_schema_jsonld', true);
        if (!is_string($schema) || trim($schema) === '') {
            return;
        }

        echo '<script type="application/ld+json">' . wp_kses_post($schema) . '</script>' . "\n";
    }

    public static function render_category_pill(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        $label = self::primary_category_label();
        if ($label === '') {
            return;
        }

        printf(
            '<div class="ebu-article-label"><span class="ebu-category-pill">%s</span></div>',
            esc_html($label)
        );
    }

    public static function open_article_stage(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        echo '<div class="ebu-article-stage">';
        self::render_side_rail('left');
        echo '<div class="ebu-article-column">';
        self::render_side_rail('mobile');
    }

    public static function close_article_stage(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        echo '</div>';
        self::render_side_rail('right');
        echo '</div>';
    }

    private static function render_side_rail(string $position): void
    {
        $blocks = self::get_side_blocks();
        $items = array_values(array_filter(
            $blocks,
            static function (array $block) use ($position): bool {
                return ($block['side'] ?? '') === $position;
            }
        ));

        if ($items === []) {
            if ($position !== 'mobile') {
                echo '<aside class="ebu-side-rail ebu-side-rail--' . esc_attr($position) . '" aria-hidden="true"></aside>';
            }
            return;
        }

        $tag = $position === 'mobile' ? 'div' : 'aside';
        $label = $position === 'mobile' ? 'Подсказки к статье' : 'Подсказки';

        printf(
            '<%1$s class="ebu-side-rail ebu-side-rail--%2$s" aria-label="%3$s">',
            $tag,
            esc_attr($position),
            esc_attr($label)
        );

        foreach ($items as $index => $block) {
            $variant = sanitize_html_class((string) ($block['variant'] ?? 'tip'));
            $tag_label = esc_html((string) ($block['tag'] ?? 'TIP'));
            $text = esc_html((string) ($block['text'] ?? ''));

            printf(
                '<div class="ebu-side-callout ebu-side-callout--%1$s" data-ebu-callout style="--ebu-delay:%2$dms"><span class="ebu-side-callout__tag">%3$s</span><p class="ebu-side-callout__text">%4$s</p></div>',
                esc_attr($variant),
                (int) $index * 90,
                $tag_label,
                $text
            );
        }

        printf('</%s>', $tag);
    }

    /** @return list<array{tag:string,text:string,variant:string,side:string}> */
    private static function get_side_blocks(): array
    {
        $post_id = get_queried_object_id();
        $topic = self::primary_category_label();
        $primary = get_post_meta($post_id, '_excalibur_blog_primary_query', true);
        if (!is_string($primary) || trim($primary) === '') {
            $primary = $topic;
        } else {
            $primary = trim($primary);
        }

        $content = get_post_field('post_content', $post_id);
        $stat_line = 'Проверьте спрос в Вордстате по главному ключу статьи перед публикацией.';
        if (is_string($content) && preg_match('/Вордстат[^.]*\./u', wp_strip_all_tags($content), $match)) {
            $stat_line = trim($match[0]);
        }

        return [
            [
                'tag'     => 'GEO',
                'text'    => 'Добавляйте термины и расшифровку рядом: это снижает «непонятность» для новых читателей.',
                'variant' => 'geo',
                'side'    => 'left',
            ],
            [
                'tag'     => 'SEO',
                'text'    => 'Проверяйте, чтобы ключ «' . $primary . '» встречался в H1, первом абзаце и одном H2.',
                'variant' => 'seo',
                'side'    => 'left',
            ],
            [
                'tag'     => 'STAT',
                'text'    => $stat_line,
                'variant' => 'stat',
                'side'    => 'right',
            ],
            [
                'tag'     => 'AI',
                'text'    => 'Начните с одного tool в AI Agent — модель путается при 10+ инструментах сразу.',
                'variant' => 'ai',
                'side'    => 'right',
            ],
        ];
    }

    public static function enhance_faq_markup(string $content): string
    {
        if (!self::is_blog_article()) {
            return $content;
        }

        if (strpos($content, 'ebu-faq-card') !== false) {
            return $content;
        }

        if (strpos($content, 'id="faq"') === false && strpos($content, "id='faq'") === false) {
            return $content;
        }

        $updated = preg_replace_callback(
            '/<h2\s+id=["\']faq["\'][^>]*>.*?<\/h2>\s*(.*)$/su',
            static function (array $matches): string {
                $body = $matches[1];
                $body = preg_replace_callback(
                    '/<h3>(.*?)<\/h3>\s*((?:<p>.*?<\/p>\s*)+)/su',
                    static function (array $item): string {
                        return '<div class="ebu-faq-card__item"><h3 class="ebu-faq-card__question">'
                            . $item[1]
                            . '</h3><div class="ebu-faq-card__answer">'
                            . $item[2]
                            . '</div></div>';
                    },
                    $body
                );

                return '<div class="ebu-faq-card" id="faq"><h2 class="ebu-faq-card__title">Часто задаваемые вопросы по теме (FAQ)</h2>'
                    . $body;
            },
            $content,
            1
        );

        return is_string($updated) ? $updated : $content;
    }

    public static function render_article_footer(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        self::render_post_navigation();
        self::render_related_posts();
        self::render_next_step();
    }

    private static function render_post_navigation(): void
    {
        $prev = get_previous_post();
        $next = get_next_post();

        if (!$prev && !$next) {
            return;
        }

        echo '<nav class="navigation post-navigation" aria-label="Записи"><div class="nav-links">';

        if ($prev instanceof WP_Post) {
            printf(
                '<div class="nav-previous"><a href="%s" rel="prev"><span class="nav-subtitle">← Предыдущая</span> <span class="nav-title">%s</span></a></div>',
                esc_url(get_permalink($prev)),
                esc_html(get_the_title($prev))
            );
        }

        if ($next instanceof WP_Post) {
            printf(
                '<div class="nav-next"><a href="%s" rel="next"><span class="nav-subtitle">Следующая →</span> <span class="nav-title">%s</span></a></div>',
                esc_url(get_permalink($next)),
                esc_html(get_the_title($next))
            );
        }

        echo '</div></nav>';
    }

    private static function render_related_posts(): void
    {
        $query = new WP_Query([
            'post_type'           => 'post',
            'post_status'         => 'publish',
            'posts_per_page'      => 3,
            'post__not_in'        => [get_the_ID()],
            'ignore_sticky_posts' => true,
            'orderby'             => 'date',
            'order'               => 'DESC',
            'no_found_rows'       => true,
        ]);

        if (!$query->have_posts()) {
            wp_reset_postdata();
            return;
        }

        echo '<section id="related-posts" class="related-posts">';
        echo '<h2 class="related-title">Читайте также</h2><div class="related-grid">';

        $gradient = 1;
        while ($query->have_posts()) {
            $query->the_post();
            $thumb = get_the_post_thumbnail_url(get_the_ID(), 'medium_large');
            echo '<article class="related-card">';
            printf('<a href="%s" class="related-card-link">', esc_url(get_permalink()));
            echo '<div class="related-thumb">';
            if (is_string($thumb) && $thumb !== '') {
                printf(
                    '<img src="%s" alt="%s" loading="lazy" decoding="async" width="480" height="270" />',
                    esc_url($thumb),
                    esc_attr(get_the_title())
                );
            } else {
                printf('<div class="img-placeholder gradient-%d" aria-hidden="true"></div>', $gradient);
                $gradient = ($gradient % 3) + 1;
            }
            echo '</div><div class="related-body">';
            printf('<h4>%s</h4>', esc_html(get_the_title()));
            printf('<span class="related-date">%s</span>', esc_html(get_the_date('d.m.Y')));
            echo '</div></a></article>';
        }

        echo '</div></section>';
        wp_reset_postdata();
    }

    private static function render_next_step(): void
    {
        $site = home_url('/');
        $primary = self::cta_url('primary');
        $primary_label = self::cta_label('primary');

        echo '<section class="article-next-step" aria-label="Следующий шаг">';
        echo '<div class="article-next-step-head">';
        echo '<h2>Что делать дальше</h2>';
        echo '<p>Выберите удобный формат продолжения: кейсы, контакт или AI-аудит.</p>';
        echo '</div><div class="article-next-step-grid">';

        printf(
            '<a href="%s#services" class="next-step-card next-step-card--case"><span class="next-step-label">Путь 01</span><h3>Разобрать больше кейсов</h3><p>Откройте материалы и соберите рабочую систему на реальных примерах внедрения AI.</p></a>',
            esc_url($site)
        );

        printf(
            '<a href="%s#contact" class="next-step-card next-step-card--channel"><span class="next-step-label">Путь 02</span><h3>Обсудить внедрение</h3><p>Расскажите о процессе — подскажем, где AI-агенты дадут быстрый эффект без лишней разработки.</p></a>',
            esc_url($site)
        );

        printf(
            '<a href="%s" class="next-step-card next-step-card--training" target="_blank" rel="noopener noreferrer"><span class="next-step-label">Путь 03</span><h3>%s</h3><p>Короткая диагностика процессов и рекомендации по стеку: n8n, Make, CRM, RAG.</p></a>',
            esc_url($primary),
            esc_html($primary_label)
        );

        echo '</div></section>';
    }

    private static function primary_category_label(): string
    {
        $post_id = get_queried_object_id();

        $meta_keys = [
            '_excalibur_blog_primary_query',
            '_excalibur_blog_topic_label',
            '_excalibur_blog_category_label',
        ];

        foreach ($meta_keys as $key) {
            $from_meta = get_post_meta($post_id, $key, true);
            if (is_string($from_meta) && trim($from_meta) !== '') {
                return trim($from_meta);
            }
        }

        $tags = get_the_tags($post_id);
        if (!empty($tags)) {
            return $tags[0]->name;
        }

        $categories = get_the_category($post_id);
        if (!empty($categories)) {
            $name = $categories[0]->name;
            if (!in_array($name, ['Без рубрики', 'Uncategorized'], true)) {
                return $name;
            }
        }

        $title = get_the_title($post_id);
        if (is_string($title) && preg_match('/^([^:—-]+)/u', $title, $matches)) {
            $short = trim($matches[1]);
            if ($short !== '' && mb_strlen($short) <= 48) {
                return $short;
            }
        }

        return 'AI Engineering';
    }

    private static function reading_time_label(): string
    {
        $content = get_post_field('post_content', get_queried_object_id());
        if (!is_string($content)) {
            return '5 мин';
        }

        $text = wp_strip_all_tags($content);
        $words = preg_match_all('/\p{L}+/u', $text, $m) ? count($m[0]) : str_word_count($text);
        $minutes = max(1, (int) ceil($words / 200));

        return $minutes . ' мин';
    }

    private static function cta_url(string $which = 'primary'): string
    {
        $map = [
            'primary'   => 'PRIMARY_CTA_URL',
            'secondary' => 'SECONDARY_CTA_URL',
        ];
        $env = $map[$which] ?? 'PRIMARY_CTA_URL';
        $from_env = getenv($env);
        if (is_string($from_env) && $from_env !== '') {
            return $from_env;
        }
        if (defined($env)) {
            $const = constant($env);
            if (is_string($const) && $const !== '') {
                return $const;
            }
        }

        $defaults = [
            'primary'   => home_url('/#contact'),
            'secondary' => home_url('/#services'),
        ];

        return $defaults[$which] ?? home_url('/');
    }

    private static function cta_label(string $which = 'primary'): string
    {
        $map = [
            'primary'   => 'PRIMARY_CTA_LABEL',
            'secondary' => 'SECONDARY_CTA_LABEL',
        ];
        $env = $map[$which] ?? 'PRIMARY_CTA_LABEL';
        $from_env = getenv($env);
        if (is_string($from_env) && $from_env !== '') {
            return $from_env;
        }
        if (defined($env)) {
            $const = constant($env);
            if (is_string($const) && $const !== '') {
                return $const;
            }
        }

        $defaults = [
            'primary'   => 'Запросить AI-аудит',
            'secondary' => 'Обсудить внедрение',
        ];

        return $defaults[$which] ?? 'Связаться';
    }
}

Excalibur_Blog_UI::init();
