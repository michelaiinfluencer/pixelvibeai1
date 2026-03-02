const footerContent = `
<div class="footer-top">
    <div class="footer-brand">
        <p>Creative AI Studio</p>
    </div>
    <div class="footer-links">
        <a href="contact.html">Contact</a>
        <a href="mailto:mail@pixelvibeai.com">mail@pixelvibeai.com</a>
    </div>
</div>
<div class="footer-bottom">© 2026 PixelVibe AI. All rights reserved.</div>
`;

document.addEventListener('DOMContentLoaded', () => {
    const placeholder = document.getElementById('footer-placeholder');
    if (placeholder) {
        placeholder.innerHTML = footerContent;
    }
});
