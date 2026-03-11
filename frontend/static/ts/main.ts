// Main TypeScript file for Sistema de Votos

interface Poll {
    id: number;
    title: string;
}

class App {
    constructor() {
        console.log("Sistema de Votos Frontend Inicializado com TypeScript!");
        this.initAnimations();
    }

    private initAnimations(): void {
        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                console.log("Hovering over a poll card");
            });
        });
    }
}

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    new App();
});
