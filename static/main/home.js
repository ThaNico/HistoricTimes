const MS_BETWEEN_UPDATES = 20000; // TODO custom setting
let timer;

$(document).ready(function () {
  setInitialTimeValue();
  timer = setInterval(increaseTimeValue, MS_BETWEEN_UPDATES);

  $("#specific-search").on("click", setSpecificTimeValue);
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
  })
    .done(function (data) {
      console.log("got", data);
    })
    .fail(function (data) {
      clearInterval(timer);
    });
};

const increaseTimeValue = () => {
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

const setSpecificTimeValue = () => {
  let hours = parseInt($("#specific-hour").val());
  let minutes = parseInt($("#specific-minute").val());
  if (hours && minutes) {
    setTimeValue(hours, minutes);
  }
};
