function toggleTheme() {
  const root = document.documentElement;
  const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  root.setAttribute('data-theme', next);
  try { localStorage.setItem('fvm-theme', next); } catch (e) {}
}

try {
  const saved = localStorage.getItem('fvm-theme');
  if (saved) document.documentElement.setAttribute('data-theme', saved);
} catch (e) {}

const hdr = document.getElementById('hdr');
if (hdr) {
  window.addEventListener('scroll', () => {
    hdr.classList.toggle('scrolled', window.scrollY > 30);
  });
}
