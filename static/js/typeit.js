new TypeIt(".banner__title", {
    speed: 150,
    loop: true,
    waitUntilVisible: true,
})
.type('<span class="SEO">SEO Xidməti</span>', {delay: 1000})
.delete('.SEO')
.type('<span class="Rəqəmsal">Rəqəmsal Strategiya</span>', {delay: 1000})
    .delete('.Rəqəmsal')
    .type('<span class="SMM">SMM Xidməti</span>', {delay: 1000})
    .delete('.SMM')
    .type('<span class="Vebsayt">Vebsayt Xidməti</span>', {delay: 1000})
    .delete('.Vebsayt')
    .type('<span class="Marketinq">360° Marketinq</span>', {delay: 1000})
    .delete('.Marketinq')
    .go();