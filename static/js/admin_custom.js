    // JavaScript для переключения приложений
    document.addEventListener('DOMContentLoaded', function() {
        const appLinks = document.querySelectorAll('.app-link');
        const modelsContainer = document.getElementById('models-container');

        appLinks.forEach(link => {
            link.addEventListener('click', function(event) {
                event.preventDefault();

                const appName = this.getAttribute('data-app-name');
                const models = JSON.parse(this.getAttribute('data-models'));

                // Очистить контейнер
                modelsContainer.innerHTML = `<h2>${this.textContent}</h2>`;

                if (models.length > 0) {
                    const ul = document.createElement('ul');
                    models.forEach(model => {
                        const li = document.createElement('li');
                        li.innerHTML = `<a href="${model.admin_url}">${model.name}</a>`;
                        ul.appendChild(li);
                    });
                    modelsContainer.appendChild(ul);
                } else {
                    modelsContainer.innerHTML += '<p>{% translate "No models available." %}</p>';
                }
            });
        });
    });