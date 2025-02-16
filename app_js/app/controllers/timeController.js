const { getCurrentMoscowTime } = require('../utils/timeUtils');

const getMoscowTime = (req, res) => {
  const moscowTime = getCurrentMoscowTime();
  res.render('moscow_time', { time: moscowTime });
};

module.exports = { getMoscowTime };