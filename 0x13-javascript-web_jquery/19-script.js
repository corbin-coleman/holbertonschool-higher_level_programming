#!/usr/bin/node
$('div#add_item').click(function () {
  $('UL.my_list').add('<LI>Item</LI>').appendTo('UL.my_list');
});
