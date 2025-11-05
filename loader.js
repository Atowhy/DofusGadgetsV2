// loader.js

/**
 * Charge un fichier HTML dans un élément de la page.
 * @param {string} elementId - L'ID de l'élément où injecter le HTML.
 * @param {string} filePath - Le chemin vers le fichier HTML à charger.
 */
async function loadComponent(elementId, filePath) {
  try {
    const response = await fetch(filePath);
    if (!response.ok) {
      throw new Error(`Le chargement a échoué: ${response.statusText}`);
    }
    const text = await response.text();
    const element = document.getElementById(elementId);
    if (element) {
      element.innerHTML = text;
    } else {
      console.warn(`L'élément avec l'ID "${elementId}" n'a pas été trouvé.`);
    }
  } catch (error) {
    console.error(`Erreur lors du chargement du composant depuis "${filePath}":`, error);
  }
}

// Ceci est un événement personnalisé que nous déclencherons lorsque le header et le footer seront chargés.
const componentsLoadedEvent = new Event('componentsLoaded');

/**
 * Fonction principale qui charge le layout (header et footer).
 */
async function loadLayout() {
  // Récupère les chemins depuis les attributs data-* sur la balise <body>
  // Permet à chaque page de spécifier où se trouvent les fichiers.
  const headerPath = document.body.dataset.headerPath || '/header.html';
  const footerPath = document.body.dataset.footerPath || '/footer.html';

  // Charge les deux en parallèle et attend que les deux soient terminés.
  await Promise.all([
    loadComponent('main-header', headerPath),
    loadComponent('main-footer', footerPath)
  ]);

  // Une fois que tout est chargé, on envoie le "signal" au reste de la page.
  console.log('Header et Footer chargés. Envoi du signal "componentsLoaded".');
  document.dispatchEvent(componentsLoadedEvent);
}

// On lance le chargement du layout dès que possible.
loadLayout();
