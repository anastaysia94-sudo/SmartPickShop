<?php
/**
 * Voltage Foundry staging-only theme setup.
 * No purchasing, membership, or private phpBB access is enabled here.
 */
if (!defined('ABSPATH')) { exit; }

function vf_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('custom-logo');
    add_theme_support('html5', array('search-form','comment-form','comment-list','gallery','caption','style','script'));
    register_nav_menus(array('primary' => __('Primary Navigation', 'voltage-foundry')));
}
add_action('after_setup_theme', 'vf_setup');

function vf_assets() {
    wp_enqueue_style('voltage-foundry-style', get_stylesheet_uri(), array(), '0.1.0');
}
add_action('wp_enqueue_scripts', 'vf_assets');

/**
 * Public URLs are blank by default; never expose the private AI-only phpBB.
 * Website admins may set verified public/community URLs in Appearance > Customize.
 */
function vf_customize_register($customizer) {
    $customizer->add_section('vf_destinations', array(
        'title' => __('Voltage Foundry destinations', 'voltage-foundry'),
        'priority' => 36,
        'description' => __('Only enter public URLs verified to work. The private AI phpBB must not be entered here.', 'voltage-foundry')
    ));
    foreach (array('vf_community_url' => 'Public MyBB community URL', 'vf_shop_url' => 'Verified public store URL') as $id => $label) {
        $customizer->add_setting($id, array('default' => '', 'sanitize_callback' => 'esc_url_raw'));
        $customizer->add_control($id, array('label' => __($label, 'voltage-foundry'), 'section' => 'vf_destinations', 'type' => 'url'));
    }
}
add_action('customize_register', 'vf_customize_register');

function vf_public_link($setting, $label) {
    $value = get_theme_mod($setting, '');
    if (!$value) { return; }
    printf('<a class="button secondary" href="%s" rel="noopener noreferrer">%s</a>', esc_url($value), esc_html($label));
}
