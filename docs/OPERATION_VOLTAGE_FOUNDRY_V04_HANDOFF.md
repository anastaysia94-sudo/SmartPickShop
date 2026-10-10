# Operation Voltage Foundry — Four Gears Website Design Handoff (v0.4)
[ChatGPT - anastaysia94] 2026-10-10 PT — **REPORTED** portable artifacts + **VERIFIED** local tests; NOT a production deployment.

## Purpose and boundaries

Operation Voltage Foundry is the visual/creative execution within SmartPickShop Holdings (P001 / XW0001; branding workstream P068 / XW0067). This handoff records a *portable* graphical design system for eventual PHP, WordPress, phpBB and other PHP-script adapters. The SmartPickShop GitHub repository itself is a cross-LLM coordination repository, **not** a confirmed deployed PHP website. Do not mistake this documentation-only PR for a website installation.

## The original brand is primary

- **Brass (steampunk)** — copper, brass, mechanical craftsmanship and workshop light.
- **Neon (cyberpunk)** — electric cyan/magenta, electronic navigation, technological signal.
- **Riot (punk rock)** — DIY music, handmade posters, rebellious but readable design.
- **Midnight (gothic)** — dark romantic archives, violet lighting and filigree.
- The first-class website lens is `foundry`. **Snarky How-To** (PG-13 graphic comic) and **Oops Academy** (kid-friendly cartoon) are *optional secondary educational treatments*, not the homepage's default identity.

## Cast and continuity

| Character | Visual continuity |
|---|---|
| Roxie Voltage | Maker and protagonist, amber eyes, inventor goggles, electric-cyan styling; keep likeness recognizable across four gears |
| Juno Mercer | Fabrication specialist; deep warm-brown skin, short black curls with a copper coil |
| Sable Reyes | Investigative archivist; olive skin, hazel eyes, sharp black bob and beauty mark beneath left eye |
| Beacon the dog | German Shepherd / Aussie / Husky mix, upright ears, narrow white forehead stripe, **cloudy gray-blue left eye**, **golden-amber right eye** |
| Three supporting partners | Anonymous specification slots only; names, approved likenesses and pairing remain unresolved |

Do not invent partner faces, relationship details or complete character approvals. A younger Oops cast description conflicts with adult-married-family Oops notes; preserve both as unresolved rather than silently deciding canon. Previously approved art is a *reference*, never copied pixel-for-pixel into new artwork.

## Evidence split

**VERIFIED locally in prior kit and v0.4 pass:** standalone CSS and JavaScript parsing, PHP syntax, demo controls in Chromium at six viewports (320, 375, 768, 1024, 1440, 1920), no detected JS exceptions or horizontal overflow, ZIP integrity and 46 packaged files with SHA-256 digest manifest. The WordPress PHP shortcode escapes untrusted text in an isolated shim test; the phpBB ribbon gear selector behaves locally.

**IMPLEMENTED BUT NOT ACCEPTED ON SITE:** opt-in `.vf-shell` design layer; generic PHP sample, WordPress companion shortcode and phpBB template-event visual extension. v0.4 makes `foundry` the default lens, relegates educational looks to optional controls, improves WordPress conditional enqueueing for ordinary shortcode pages, and guards repeat initialization of CSS/JS components. These are not yet tested inside a real installed CMS.

**REPORTED prior source graphics:** an existing FG01–FG21 batch was generated/uploaded and indexed in the source asset index. This v0.4 handoff does not re-verify all files or claim that newly planned art has been generated. The 64-slot graphic matrix is **SPEC ONLY** (32 main character/lens/gear, 24 anonymous partners, 8 ensemble).

**OPEN / NOT IMPLEMENTED:** confirmed site/server/theme mapping, staging backup, WordPress/phpBB/MyBB installation, live CMS tests and role permissions, founder-only-human phpBB LLM posting rules, public MyBB user flows, authentication boundaries, final partner portraits, final graphic approvals, performance/a11y multi-device testing, deployment, social publication, buyer acceptance and revenues.

## Source-of-truth pointers

- [Operation Voltage Foundry current runbook](https://drive.google.com/file/d/1Kf_UpPEOMRwaStJhFTvMS3p-lKG8xotT/view)
- [FG01–FG21 original asset reference index](https://drive.google.com/file/d/1AwR2H2V7BJnYqWgiYU02hprWh-bMNp5g/view)
- [Four Gears asset batch folder](https://drive.google.com/drive/folders/1dZLPwWCCPf5ofDM-ngT6Ry_AuZtYwGpp)
- [Rebrand visual manifest](https://docs.google.com/spreadsheets/d/154yiQxqPjhHgZ94pYvqkqhH6zV5vKnKyllhY92v57FI/edit)
- [Corporate Hieroglyphics Definitions Wiki](https://docs.google.com/document/d/1g0hGwNzlYbS31OZ7AsO_R2uibTyoPfQkWWqCc_6VEmQ/edit)
- The current v0.4 ZIP and QA artifacts were delivered through the ChatGPT conversation; do not assume the ZIP has been mirrored to GitHub or Drive.

## Next safe actions

1. Identify which deployed site and server/repository actually host each of the main WordPress, public MyBB and private LLM-only phpBB surfaces. Do **not** replace the contents of this coordination repo with a CMS.
2. Confirm staging, backups, restore procedure and current PHP/CMS/plugin/theme versions. Install *one compatible adapter* in staging only.
3. Test UI and permissions independently: guest, member, founder/admin and permitted LLM service accounts; do not enforce access via CSS alone.
4. Verify original cast art and supporting partner references; generate and approve genuinely new homepage scenes in Four Gears priority order, including Beacon.
5. Verify content, mobile layouts, keyboard/screen-reader accessibility, performance, link integrity, restore rehearsal, actual installation and owner release decision before labeling any site as live.
6. Update canonical ledger and cross-LLM handoff with readback proof; preserve older authors' prefixes and machine-clean IDs.

**Project tracking rule:** proposed / coded / rendered / uploaded / tested / installed / published / sold / paid are different evidence states.
