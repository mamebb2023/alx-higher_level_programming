#!/usr/bin/node
$(document).ready(() => {
  $('DIV#toggle_header').click(() => {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
