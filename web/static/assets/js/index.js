
    //  mode dark pour les gens qui ne sortent pas de chez eux voir la lumiere du jours
    document.getElementById("toggle-darkmode").onclick = () => {
      document.body.classList.toggle("dark");
    };
  
    // profil
    document.querySelector(".profile-menu").addEventListener("click", (e) => {
      e.stopPropagation();
      document.querySelector(".profile-menu").classList.toggle("active");
    });
  
    // notif
    document.querySelector(".notification").addEventListener("click", (e) => {
      e.stopPropagation();
      document.querySelector(".notification").classList.toggle("active");
    });
  
    // syteme contact
    const contactOptions = document.querySelectorAll('.contact-option:not(.expandable)');
    const contactModal = document.getElementById('contactModal');
    const recipientName = document.getElementById('recipient-name');
    const cancelBtn = document.getElementById('cancel-message');
    const sendBtn = document.getElementById('send-message');
    const dropdown = document.querySelector('.dropdown');
    const nestedDropdowns = document.querySelectorAll('.nested-dropdown');
  
    //menu princ
    dropdown.addEventListener('click', (e) => {
      e.stopPropagation();
      const content = dropdown.querySelector('.dropdown-content');
      content.style.display = content.style.display === 'block' ? 'none' : 'block';
    });
  
    // Gestion des sous-menus
    nestedDropdowns.forEach(dropdown => {
      dropdown.addEventListener('click', (e) => {
        e.stopPropagation();
        const nestedContent = dropdown.querySelector('.nested-content');
        nestedContent.style.display = nestedContent.style.display === 'block' ? 'none' : 'block';
      });
    });
  
    // Fermer les menus quand on clique ailleurs
    document.addEventListener('click', () => {
      document.querySelector('.dropdown-content').style.display = 'none';
      document.querySelectorAll('.nested-content').forEach(el => {
        el.style.display = 'none';
      });
    });
  
    contactOptions.forEach(option => {
      option.addEventListener('click', (e) => {
        e.preventDefault();
        if (option.dataset.role) {
          recipientName.textContent = option.dataset.role;
          contactModal.style.display = 'block';
        }
      });
    });
  
    document.querySelector('.close-modal').addEventListener('click', () => {
      contactModal.style.display = 'none';
    });
  
    cancelBtn.addEventListener('click', () => {
      contactModal.style.display = 'none';
    });
  
    sendBtn.addEventListener('click', () => {
      const message = document.getElementById('message-content').value;
      if (message.trim() !== '') {
        contactModal.style.display = 'none';
        document.getElementById('message-content').value = '';
      }
    });
  
    // Fermer la modale si on clique en dehors
    window.addEventListener('click', (e) => {
      if (e.target === contactModal) {
        contactModal.style.display = 'none';
      }
    });