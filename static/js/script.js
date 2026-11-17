/**
 * Smart Lost and Found System – Interactive Script
 * Directly from Internship Report Chapter 7.2 (Page 21):
 * 1. Form validation before submission
 * 2. Instant live search filtering as user types
 * 3. Active navigation link state handling
 */

document.addEventListener('DOMContentLoaded', () => {
  // =========================================================================
  // 1. Validate the report form before submitting (Report Page 21)
  // =========================================================================
  const form = document.getElementById('report-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      const itemInput = document.getElementById('item');
      const placeInput = document.getElementById('place');

      const item = itemInput ? itemInput.value.trim() : '';
      const place = placeInput ? placeInput.value.trim() : '';

      if (item === '' || place === '') {
        e.preventDefault();
        alert('Please enter the item name and the place.');
        if (item === '' && itemInput) {
          itemInput.focus();
        } else if (placeInput) {
          placeInput.focus();
        }
        return false;
      }
    });
  }

  // =========================================================================
  // 2. Filter the item cards while typing in the search box (Report Page 21)
  // =========================================================================
  const searchInputs = document.querySelectorAll('#search, #main-search-input, .live-search-input');
  searchInputs.forEach(search => {
    search.addEventListener('input', () => {
      const text = search.value.toLowerCase().trim();
      const cards = document.querySelectorAll('.report-item-card, .item-card');
      let visibleCount = 0;

      cards.forEach(card => {
        const match = card.textContent.toLowerCase().includes(text);
        card.style.display = match ? '' : 'none';
        if (match) visibleCount++;
      });

      // Update empty state if element exists
      const noResultsMsg = document.getElementById('no-search-results');
      if (noResultsMsg) {
        noResultsMsg.style.display = (visibleCount === 0 && text !== '') ? 'block' : 'none';
      }
    });
  });

  // =========================================================================
  // 3. Highlight the active navigation link (Report Page 21)
  // =========================================================================
  const navLinks = document.querySelectorAll('.nav-links a:not(.btn-nav-login):not(.btn-nav-logout)');
  navLinks.forEach(link => {
    // Check if the current URL matches href
    if (window.location.pathname === link.getAttribute('href')) {
      navLinks.forEach(a => a.classList.remove('active'));
      link.classList.add('active');
    }

    link.addEventListener('click', () => {
      navLinks.forEach(a => a.classList.remove('active'));
      link.classList.add('active');
    });
  });

  // Image upload preview helper
  const photoInput = document.getElementById('photo');
  if (photoInput) {
    photoInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        const previewText = document.getElementById('file-chosen-text');
        if (previewText) {
          previewText.textContent = `Selected: ${file.name}`;
        }
      }
    });
  }
});
