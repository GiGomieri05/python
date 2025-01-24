// Função para carregar as missões dinamicamente
function loadMissions() {
    const missionsList = document.querySelector('.missions-list');
    const missions = [
        { name: 'Missão 1', color: '#ff5733' },
        { name: 'Missão 2', color: '#33c3ff' },
        { name: 'Missão 3', color: '#28a745' }
    ];

    missions.forEach(mission => {
        const missionDiv = document.createElement('div');
        missionDiv.classList.add('mission-item');
        missionDiv.style.backgroundColor = mission.color;

        missionDiv.innerHTML = `
            <div class="mission-content">
                <h3>${mission.name}</h3>
            </div>
        `;
        missionsList.appendChild(missionDiv);
    });
}

// Chama a função ao carregar a página
window.onload = loadMissions;
