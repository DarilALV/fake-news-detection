document.addEventListener('DOMContentLoaded', function () {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            const targetTab = this.getAttribute('data-tab');

            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));

            this.classList.add('active');
            document.querySelector(`[data-content="${targetTab}"]`).classList.add('active');
        });
    });

    const form = document.getElementById('analyze-form');
    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            alert('Sprint 1 — El modelo de IA estará operativo a partir del Sprint 3 (1 de junio). Esta es la interfaz definitiva.');
        });
    }
});
