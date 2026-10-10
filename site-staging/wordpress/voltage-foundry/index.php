<?php
if (!defined('ABSPATH')) { exit; }
get_header();
?>
<section class="panel-section"><div class="container">
  <div class="section-intro"><span class="eyebrow">Public editorial</span><h1><?php echo esc_html(get_bloginfo('name')); ?> — Stories</h1></div>
  <?php
  if (have_posts()) {
      while (have_posts()) {
          the_post();
          echo '<article class="entry"><h2><a href="'.esc_url(get_permalink()).'">'.esc_html(get_the_title()).'</a></h2>';
          the_excerpt();
          echo '</article>';
      }
      the_posts_pagination();
  } else {
      echo '<p>No published articles yet.</p>';
  }
  ?>
</div></section>
<?php get_footer(); ?>
