const MS_BETWEEN_UPDATES = 10000;
let timer = null;

$(document).ready(function () {
  setInitialTimeValue();
  createTimer();

  $("#specific-search").on("click", setSpecificTimeValue);
  $("#specific-hour, #specific-minute").on("keydown", function search(e) {
    if (e.keyCode == 13) {
      setSpecificTimeValue();
    }
  });

  $("#play").on("click", createTimer);
  $("#pause").on("click", stopTimer);
});

const setInitialTimeValue = () => {
  var current = new Date();
  setTimeValue(current.getHours(), current.getMinutes());
};

const createTimer = () => {
  stopTimer();
  timer = setInterval(increaseTimeValue, MS_BETWEEN_UPDATES);
  $("#time-container .time-separator").addClass("blink");
  togglePausePlayButtons(false);
};

const stopTimer = () => {
  if (timer) {
    clearInterval(timer);
  }
  $("#time-container .time-separator").removeClass("blink");
  togglePausePlayButtons(true);
};

const togglePausePlayButtons = (displayPlay) => {
  $("#play").toggle(displayPlay);
  $("#pause").toggle(!displayPlay);
};

const setTimeValue = (hours, minutes) => {
  $("#hours").text(pad2numbers(hours));
  $("#minutes").text(pad2numbers(minutes));
  fetchEvents();
};

const pad2numbers = (number) =>
  number.toLocaleString(undefined, { minimumIntegerDigits: 2 });

const fetchEvents = () => {
  const hours = $("#hours").text();
  const cachedData = getCachedHour(hours);
  if (cachedData !== null) {
    fillEventData(cachedData);
    return;
  }

  stopTimer();
  $.ajax({
    method: "GET",
    url: `/events/${hours}`,
  }).done(function (data) {
    createTimer();
    setCachedHour(hours, data);
    fillEventData(data);
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
  if (!isNaN(hours) && !isNaN(minutes)) {
    setTimeValue(hours, minutes);
  }
};

const fillEventData = (data) => {
  const container = $("#events-container");
  container.empty();

  const key = `${$("#hours").text()}:${$("#minutes").text()}:00`;
  if (!(key in data)) {
    container.text("There are no events to display for this time.");
    return;
  }

  for (const event of data[key]) {
    const eventLine = $("#event-template").clone().removeAttr("id");
    eventLine.find(".event-text").text(event["label"]);
    eventLine.find(".event-source").text(event["source"]);
    eventLine.find(".event-source").attr("href", event["source"]);
    eventLine.appendTo(container);
  }
};

const getCachedHour = (hour) => {
  return JSON.parse(localStorage.getItem(`events_${hour}`));
};

const setCachedHour = (hour, data) => {
  localStorage.setItem(`events_${hour}`, JSON.stringify(data));
};
