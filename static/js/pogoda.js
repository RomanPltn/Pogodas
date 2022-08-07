const IMAGE_MAP = {
  morning: 'https://i.ibb.co/2MxLpc7/1.jpg',
  day: 'https://i.ibb.co/JBfFTG4/2.jpg',
  evening: 'https://i.ibb.co/WBzHkg3/3.jpg',
  night: 'https://i.ibb.co/F4ST6LL/4.jpg',
}

const getDayPeriod = (hours) => {
  if (hours >= 6 && hours < 12) {
    return 'morning'
  } else if (hours >= 12 && hours < 17) {
    return 'day'
  } else if (hours >= 17 && hours < 21) {
    return 'evening'
  } else {
    return 'night'
  }
}

const period = getDayPeriod(new Date().getHours())
document.body.style.backgroundImage = `url('${IMAGE_MAP[period]}')`