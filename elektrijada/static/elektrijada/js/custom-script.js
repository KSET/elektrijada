
$(document).ready(function() {

  //Bootstrap tooltip
  // invoke by adding _tooltip to a tags (this makes it validate)
  $('body').tooltip({
    selector: "a[class*=_tooltip]"
  });

  //Bootstrap popover
  // invoke by adding _popover to a tags (this makes it validate)
  $('body').popover({
    selector: "a[class*=_popover]",
    trigger: "hover"
  });

  // Bootstrap rowlink
  $('tbody.rowlink').rowlink();

  // change django-endless-pagination to bootstrap pagination
  $('#rube_pagination').children().each(function() {
    if ($(this).is('a')) {
      var text = $(this).html();
      var href = $(this).attr('href');
      $('#bootstrap_pagination').append('<li><a href="'+href+'">'+text+'</li>');
    } else {
      if ($(this).hasClass('endless_page_current')) {
        var text = $(this).children(':first').html();
        $('#bootstrap_pagination').append('<li class="active"><a href="#">'+text+'</li>');
      } else if ($(this).hasClass('endless_separator')) {
        var text = $(this).html();
        $('#bootstrap_pagination').append('<li class="disabled"><a href="#">'+text+'</li>');
      }
    }
  });
  $('#rube_pagination').hide();

});
