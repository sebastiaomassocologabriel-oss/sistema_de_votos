// Compiled JavaScript from main.ts (Placeholder for demonstration)
class App {
    constructor() {
        console.log("Sistema de Votos Frontend Inicializado (JS compilado de TS)!");
        this.initAnimations();
        this.initProgressBars();
    }
    initAnimations() {
        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                console.log("Hovering over a poll card");
            });
        });
    }
    initProgressBars() {
        const progressBars = document.querySelectorAll('.progress-bar');
        progressBars.forEach(bar => {
            const width = bar.dataset.width;
            if (width) {
                bar.style.width = width + '%';
            }
        });
    }
}
document.addEventListener('DOMContentLoaded', () => {
    new App();
});
