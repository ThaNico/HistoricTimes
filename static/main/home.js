const MS_BETWEEN_UPDATES = 20000; // TODO custom setting

$(document).ready(function () {
  setInitialTimeValue();
  setInterval(increaseTime, MS_BETWEEN_UPDATES);
});

const setInitialTimeValue = () => {
  var current = new Date();
  setTimeValue(current.getHours(), current.getMinutes());
};

const setTimeValue = (hours, minutes) => {
  $("#events-container").empty();
  $("#hours").text(pad2numbers(hours));
  $("#minutes").text(pad2numbers(minutes));
  fetchEvents();
};

const pad2numbers = (number) =>
  number.toLocaleString(undefined, { minimumIntegerDigits: 2 });

const fetchEvents = () => {
  const hours = $("#hours").text();
  const minutes = $("#minutes").text();
  const urlToFetch = `/events/${hours}/${minutes}`;
  $.ajax({
    method: "GET",
    url: urlToFetch,
  }).done(function (data) {
    console.log("got", data);
  });
};

const increaseTime = () => {
  let hours = parseInt($("#hours").text());
  let minutes = parseInt($("#minutes").text());
  minutes++;
  if (minutes > 59) {
    minutes = 0;
    hours++;
    if (hours > 23) {
      hours = 0;
    }
  }
  setTimeValue(hours, minutes);
};
