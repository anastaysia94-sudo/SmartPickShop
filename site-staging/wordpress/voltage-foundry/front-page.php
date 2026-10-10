<?php
if (!defined('ABSPATH')) { exit; }
get_header();
?>
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">A creative workshop for practical ideas</span>
      <h1>Built in <em>four gears.</em> Made for what comes next.</h1>
      <p>SmartPickShop USA Holdings brings together experimental software, practical services, original stories and a vivid industrial world. Explore the work as it is reviewed and released.</p>
      <div class="actions">
        <a class="button" href="#gears">Discover the Four Gears</a>
        <a class="button secondary" href="#projects">Explore the work</a>
      </div>
    </div>
    <div class="emblem" aria-label="Decorative Voltage Foundry brass and neon insignia">
      <strong aria-hidden="true">V</strong><small aria-hidden="true">FOUNDRY</small>
    </div>
  </div>
</section>
<section id="gears" class="panel-section">
  <div class="container">
    <div class="section-intro"><span class="eyebrow">The original creative universe</span><h2>One world. Four distinctive signatures.</h2>
      <p>The same cast and ideas move through four expressive styles. Original source art is preserved; alternate treatments are companion works, not replacements.</p></div>
    <div class="gears">
      <article class="gear gear-brass"><span>01 · Steampunk</span><h3>Brass</h3><p>Mechanisms, copper, clockwork, ingenuity and warm industrial craft.</p></article>
      <article class="gear gear-neon"><span>02 · Cyberpunk</span><h3>Neon</h3><p>Electric cyan, midnight circuitry, digital futures and high-voltage ideas.</p></article>
      <article class="gear gear-riot"><span>03 · Punk Rock</span><h3>Riot</h3><p>DIY energy, expressive textures, music and rebellious handmade design.</p></article>
      <article class="gear gear-midnight"><span>04 · Gothic</span><h3>Midnight</h3><p>Violet shadows, archival mysteries and atmospheric storytelling.</p></article>
    </div>
  </div>
</section>
<section id="projects" class="panel-section">
  <div class="container">
    <div class="section-intro"><span class="eyebrow">The workshop</span><h2>Ideas moving toward the real world</h2>
      <p>Each project has its own readiness checks. A concept, prototype or preview should never be mistaken for a released product.</p></div>
    <div class="feature-grid">
      <article class="feature"><h3>Tools & software</h3><p>Workflows, experiments and applications developed against real-world tests.</p></article>
      <article class="feature"><h3>Creative studio</h3><p>Roxie Voltage, Juno Mercer, Sable Reyes, Beacon and their expanding cast across four aesthetics.</p></article>
      <article class="feature"><h3>Useful services</h3><p>Bounded service concepts being prepared for clear scopes, honest delivery and customer acceptance.</p></article>
    </div>
    <p class="note">Staging preview only. Product listings, availability, payments and customer accounts are intentionally not activated by this theme.</p>
    <div class="actions"><?php vf_public_link('vf_community_url', 'Visit the public community'); ?><?php vf_public_link('vf_shop_url', 'Visit the verified store'); ?></div>
  </div>
</section>
<section id="stories" class="panel-section">
  <div class="container">
    <div class="section-intro"><span class="eyebrow">Latest from the workshop</span><h2>Stories, not placeholders pretending to be news</h2></div>
    <?php
      $latest = new WP_Query(array('post_type' => 'post','post_status' => 'publish','posts_per_page' => 3,'ignore_sticky_posts' => true));
      if ($latest->have_posts()) {
          while ($latest->have_posts()) {
              $latest->the_post();
              echo '<article class="entry"><h3><a href="'.esc_url(get_permalink()).'">'.esc_html(get_the_title()).'</a></h3>';
              echo '<p>'.esc_html(wp_trim_words(get_the_excerpt(), 32)).'</p></article>';
          }
          wp_reset_postdata();
      } else {
          echo '<p class="note">Editorial work is in preparation. No unpublished draft is shown as a live article.</p>';
      }
    ?>
  </div>
</section>
<?php get_footer(); ?>
