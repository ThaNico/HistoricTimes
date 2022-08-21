const MS_BETWEEN_UPDATES = 10000;
const MS_CACHE_DURATION = 7200_000; // 2h
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
  $(".time-mover").on("click", moveTime);
});

const setInitialTimeValue = () => {
  const current = new Date();
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
  const key = `events_${hour}`;
  const item = JSON.parse(localStorage.getItem(key));
  if (!item) {
    return null;
  }

  const current = new Date();
  if (current.getTime() > item.maxage) {
    localStorage.removeItem(key);
    return null;
  }
  return item.data;
};

const setCachedHour = (hour, data) => {
  const current = new Date();
  const item = {
    data: data,
    maxage: current.getTime() + MS_CACHE_DURATION,
  };
  localStorage.setItem(`events_${hour}`, JSON.stringify(item));
};

const moveTime = () => {
  console.log("aaaa");
};
