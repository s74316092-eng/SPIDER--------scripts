const DATA_URL = 'scripts.json';

async function carregarScripts() {
    const container = document.getElementById('scripts-container');
    const loading = document.getElementById('loading');
    try {
        const resposta = await fetch(DATA_URL);
        const dados = await resposta.json();
        const scripts = dados.scripts || [];
        container.innerHTML = '';
        if (scripts.length === 0) {
            container.innerHTML = '<p style="text-align:center;">Nenhum script encontrado.</p>';
            loading.style.display = 'none';
            return;
        }
        scripts.forEach(script => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `
                ${script.imagem ? `<img src="${script.imagem}" alt="${script.titulo}" onerror="this.style.display='none'">` : ''}
                <h2>${script.titulo}</h2>
                <p class="fonte">Fonte: ${script.fonte}</p>
                <a href="${script.link}" target="_blank" rel="noopener noreferrer">Abrir script</a>
            `;
            container.appendChild(card);
        });
    } catch (erro) {
        container.innerHTML = '<p style="text-align:center;">Erro ao carregar scripts. Tente novamente mais tarde.</p>';
    } finally {
        loading.style.display = 'none';
    }
}

carregarScripts();
