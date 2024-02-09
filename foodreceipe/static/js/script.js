document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    //modal initialization
    var modals = document.querySelectorAll('.modal');
    instances = M.Modal.init(modals);

    var selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
  });
