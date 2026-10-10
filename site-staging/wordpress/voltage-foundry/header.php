<?php if (!defined('ABSPATH')) { exit; } ?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo('charset'); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="screen-reader-text" href="#main"><?php esc_html_e('Skip to content', 'voltage-foundry'); ?></a>
<div class="vf-topline" aria-hidden="true"></div>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="<?php echo esc_url(home_url('/')); ?>">
      <?php echo esc_html(get_bloginfo('name') ?: 'SmartPickShop USA Holdings'); ?>
      <span>Operation Voltage Foundry</span>
    </a>
    <nav aria-label="<?php esc_attr_e('Main navigation', 'voltage-foundry'); ?>">
      <?php
      if (has_nav_menu('primary')) {
          wp_nav_menu(array('theme_location' => 'primary', 'container' => false, 'menu_class' => 'nav-list', 'fallback_cb' => false));
      } else {
          echo '<ul class="nav-list">';
          foreach (array('gears' => 'Four Gears', 'projects' => 'Projects', 'stories' => 'Stories') as $anchor => $label) {
              printf('<li><a href="%s">%s</a></li>', esc_url(home_url('/#' . $anchor)), esc_html($label));
          }
          echo '</ul>';
      }
      ?>
    </nav>
  </div>
</header>
<main id="main">
