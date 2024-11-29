document.getElementById('participate-button').addEventListener('click', function() {
  document.getElementById('participation-modal').style.display = 'block';
});

document.querySelector('.close').addEventListener('click', function() {
  document.getElementById('participation-modal').style.display = 'none';
});

document.getElementById('create-team-button').addEventListener('click', function() {
  window.location.href = '/create-team/'; // Замените на ваш URL
  document.getElementById('participation-modal').style.display = 'none';
});

document.getElementById('find-team-button').addEventListener('click', function() {
  window.location.href = '/find-team/'; // Замените на ваш URL
  document.getElementById('participation-modal').style.display = 'none';
});

window.addEventListener('click', function(event) {
  if (event.target === document.getElementById('participation-modal')) {
    document.getElementById('participation-modal').style.display = 'none';
  }
});