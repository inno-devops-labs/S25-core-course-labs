const { format } = require('date-fns');
const { toZonedTime } = require('date-fns-tz');

const getCurrentMoscowTime = () => {
  const now = new Date();
  const moscowTime = toZonedTime(now, 'Europe/Moscow');
  return format(moscowTime, 'yyyy-MM-dd HH:mm:ss');
};

module.exports = { getCurrentMoscowTime };