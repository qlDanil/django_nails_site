$('.carousel').carousel(
    {
        interval: 7000
    });

$('a.nav-link').click(function (events) {
    if (document.location.pathname == "/works/" && !(this.hash == "#gallery" || this.hostname == "www.instagram.com")) {
        events.preventDefault();
        document.location.href = '/' + this.hash;
    }
});
