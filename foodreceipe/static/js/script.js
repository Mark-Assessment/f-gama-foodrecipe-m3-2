document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    //modal initialization
    var modals = document.querySelectorAll('.modal');
    instances = M.Modal.init(modals);

    //select initialization
    var selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

     // collapsible initializataion
     let collapsibles = document.querySelectorAll(".collapsible");
     M.Collapsible.init(collapsibles);
  });
