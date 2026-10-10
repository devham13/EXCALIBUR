<?php
/**
 * WP-CLI runner: reads JSON payload path from EXCALIBUR_PAYLOAD_FILE (absolute path).
 * Same logic as excalibur_blog_wp_publish.py bootstrap (wp-load.php context).
 */
require __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/file.php';
require_once ABSPATH . 'wp-admin/includes/media.php';
require_once ABSPATH . 'wp-admin/includes/image.php';
require_once ABSPATH . 'wp-admin/includes/post.php';

$path = getenv('EXCALIBUR_PAYLOAD_FILE');
if (!$path || !is_readable($path)) {
    echo 'ERR payload file missing or unreadable' . PHP_EOL;
    exit(1);
}
$p = json_decode(file_get_contents($path), true);
if (!is_array($p)) {
    echo 'ERR invalid payload json' . PHP_EOL;
    exit(1);
}

$slug = $p['slug'];
$existing = get_page_by_path($slug, OBJECT, 'post');
if ($existing instanceof WP_Post) {
    $post_id = (int) $existing->ID;
    wp_update_post([
        'ID' => $post_id,
        'post_title' => $p['title'],
        'post_name' => $slug,
        'post_content' => $p['content'],
        'post_excerpt' => $p['excerpt'],
        'post_status' => 'publish',
    ]);
} else {
    $post_id = (int) wp_insert_post([
        'post_title' => $p['title'],
        'post_name' => $slug,
        'post_content' => $p['content'],
        'post_excerpt' => $p['excerpt'],
        'post_status' => 'publish',
        'post_type' => 'post',
    ], true);
}
if (is_wp_error($post_id)) {
    echo 'ERR post: ' . $post_id->get_error_message() . PHP_EOL;
    exit(1);
}
echo 'OK post=' . $post_id . ' slug=' . $slug . PHP_EOL;

if (!empty($p['cover_b64'])) {
    $bin = base64_decode($p['cover_b64']);
    $tmp = wp_tempnam('excalibur-cover-' . $slug . '.png');
    file_put_contents($tmp, $bin);
    $file_array = [
        'name' => $slug . '-cover.png',
        'tmp_name' => $tmp,
        'type' => 'image/png',
        'error' => 0,
        'size' => strlen($bin),
    ];
    $att_id = media_handle_sideload($file_array, $post_id, null, [
        'post_title' => $slug . ' cover',
    ]);
    if (is_wp_error($att_id)) {
        echo 'WARN cover: ' . $att_id->get_error_message() . PHP_EOL;
    } else {
        set_post_thumbnail($post_id, (int) $att_id);
        if (!empty($p['cover_alt'])) {
            update_post_meta((int) $att_id, '_wp_attachment_image_alt', sanitize_text_field($p['cover_alt']));
        }
        echo 'OK featured_image=' . (int) $att_id . PHP_EOL;
    }
    @unlink($tmp);
}

if (!empty($p['schema_jsonld'])) {
    update_post_meta($post_id, '_excalibur_blog_schema_jsonld', wp_slash($p['schema_jsonld']));
    update_post_meta($post_id, '_excalibur_blog_skip_theme_faq', '1');
    echo 'OK schema_meta=1' . PHP_EOL;
    echo 'OK skip_theme_faq_meta=1' . PHP_EOL;
}

if (!empty($p['inline_images'])) {
    $content_updated = $p['content'];
    foreach ($p['inline_images'] as $img) {
        $bin = base64_decode($img['b64']);
        $filename = $img['filename'];
        $src = $img['src'];

        $tmp = wp_tempnam('excalibur-inline-' . $slug . '-' . sanitize_title($filename));
        file_put_contents($tmp, $bin);

        $file_array = [
            'name' => $slug . '-' . $filename,
            'tmp_name' => $tmp,
            'type' => 'image/png',
            'error' => 0,
            'size' => strlen($bin),
        ];

        $att_id = media_handle_sideload($file_array, $post_id, null, [
            'post_title' => $slug . ' ' . pathinfo($filename, PATHINFO_FILENAME),
        ]);

        if (is_wp_error($att_id)) {
            echo 'WARN inline_img_upload: ' . $att_id->get_error_message() . ' for ' . $src . PHP_EOL;
        } else {
            $new_url = wp_get_attachment_url((int) $att_id);
            if ($new_url) {
                $content_updated = str_replace('src="' . $src . '"', 'src="' . $new_url . '"', $content_updated);
                $content_updated = str_replace("src='" . $src . "'", "src='" . $new_url . "'", $content_updated);
                echo 'OK inline_image_upload=' . (int) $att_id . ' src=' . $src . ' url=' . $new_url . PHP_EOL;
            }
        }
        @unlink($tmp);
    }
    wp_update_post([
        'ID' => $post_id,
        'post_content' => $content_updated,
    ]);
}

$permalink = get_permalink($post_id);
echo 'permalink=' . $permalink . PHP_EOL;
