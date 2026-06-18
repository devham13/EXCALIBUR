<?php
/**
 * Plugin Name: Excalibur Blog UI
 * Description: AI Dev Editorial Interface — оформление технических статей блога.
 * Version: 2.0.0
 * Author: Excalibur BLOG
 * Text Domain: excalibur-blog-ui
 */

declare(strict_types=1);

if (!defined('ABSPATH')) {
    exit;
}

define('EBU_VERSION', '2.0.0');
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
        add_action('kadence_single_after_entry_header', [self::class, 'render_hero_deck'], 8);
        add_action('kadence_single_before_entry_content', [self::class, 'open_editorial_layout'], 3);
        add_action('kadence_single_after_entry_content', [self::class, 'close_editorial_layout'], 99);
        add_action('kadence_single_after_content', [self::class, 'render_article_footer'], 8);
        add_action('wp_footer', [self::class, 'render_floating_actions'], 20);
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

    public static function render_hero_deck(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        $title = get_the_title();
        $slug = sanitize_title($title);
        $panel_title = $slug !== '' ? $slug : 'article-setup';

        echo '<div class="ebu-hero-deck ebu-reveal-item">';
        echo '<div class="ebu-flow-line" aria-hidden="true">';
        echo '<span class="ebu-flow-line__node">Cursor</span>';
        echo '<span class="ebu-flow-line__arrow">→</span>';
        echo '<span class="ebu-flow-line__node">MCP</span>';
        echo '<span class="ebu-flow-line__arrow">→</span>';
        echo '<span class="ebu-flow-line__node">Tools</span>';
        echo '<span class="ebu-flow-line__arrow">→</span>';
        echo '<span class="ebu-flow-line__node">Result</span>';
        echo '</div>';

        echo '<div class="ebu-hero-panel">';
        echo '<div class="ebu-badges">';
        echo '<span class="ebu-badge">Local</span>';
        echo '<span class="ebu-badge">Secure</span>';
        echo '<span class="ebu-badge">Fast setup</span>';
        echo '<span class="ebu-badge">Low-code</span>';
        echo '</div>';

        echo '<div class="ebu-config-panel" role="presentation">';
        echo '<div class="ebu-config-panel__bar">';
        echo '<span class="ebu-config-panel__dots" aria-hidden="true"><span></span><span></span><span></span></span>';
        echo '<span class="ebu-config-panel__title">' . esc_html($panel_title) . '</span>';
        echo '</div>';
        echo '<div class="ebu-config-panel__body">';
        echo '<div class="ebu-config-panel__row"><span class="ebu-config-panel__key">Status</span><span class="ebu-config-panel__val ebu-config-panel__val--ok">connected</span></div>';
        echo '<div class="ebu-config-panel__row"><span class="ebu-config-panel__key">Tools</span><span class="ebu-config-panel__val">4 active</span></div>';
        echo '<div class="ebu-config-panel__row"><span class="ebu-config-panel__key">Mode</span><span class="ebu-config-panel__val">local server</span></div>';
        echo '<div class="ebu-config-panel__code">{"mcp": true, "agents": "ready"}</div>';
        echo '</div></div>';
        echo '</div></div>';
    }

    public static function open_editorial_layout(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        echo '<div class="ebu-editorial-layout" id="article-toc">';
        echo '<aside class="ebu-toc-rail" aria-label="Оглавление статьи">';
        echo '<div class="ebu-toc-rail__card">';
        echo '<p class="ebu-toc-rail__title">В статье</p>';
        echo '<ul class="ebu-toc-rail__list" id="ebu-toc-rail-list"></ul>';
        echo '</div></aside>';
        echo '<div class="ebu-article-main">';
    }

    public static function close_editorial_layout(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        echo '</div></div>';
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
            echo '<article class="related-card ebu-reveal-item">';
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
            '<a href="%s#services" class="next-step-card next-step-card--case ebu-reveal-item"><span class="next-step-label">Путь 01</span><h3>Разобрать больше кейсов</h3><p>Откройте материалы и соберите рабочую систему на реальных примерах внедрения AI.</p></a>',
            esc_url($site)
        );

        printf(
            '<a href="%s#contact" class="next-step-card next-step-card--channel ebu-reveal-item"><span class="next-step-label">Путь 02</span><h3>Обсудить внедрение</h3><p>Расскажите о процессе — подскажем, где AI-агенты дадут быстрый эффект без лишней разработки.</p></a>',
            esc_url($site)
        );

        printf(
            '<a href="%s" class="next-step-card next-step-card--training ebu-reveal-item" target="_blank" rel="noopener noreferrer"><span class="next-step-label">Путь 03</span><h3>%s</h3><p>Короткая диагностика процессов и рекомендации по стеку: n8n, Make, CRM, RAG.</p></a>',
            esc_url($primary),
            esc_html($primary_label)
        );

        echo '</div></section>';
    }

    public static function render_floating_actions(): void
    {
        if (!self::is_blog_article()) {
            return;
        }

        $primary = self::cta_url('primary');
        $primary_label = self::cta_label('primary');

        echo '<div class="floating-article-actions" data-floating-actions hidden>';
        echo '<a href="#related-posts" class="btn btn-secondary">Похожие материалы</a>';
        printf(
            '<a href="%s" class="btn btn-primary" target="_blank" rel="noopener noreferrer">%s</a>',
            esc_url($primary),
            esc_html($primary_label)
        );
        echo '</div>';
    }

    private static function primary_category_label(): string
    {
        $categories = get_the_category();
        if (!empty($categories)) {
            return $categories[0]->name;
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
