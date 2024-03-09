export const getWeekendDate = (): string => {
  const today = new Date();
  const dayOfWeek = today.getDay();

  let daysUntilWeekend: number;

  if (dayOfWeek === 0) {
    daysUntilWeekend = 0;
  } else if (dayOfWeek === 6) {
    daysUntilWeekend = 1;
  } else {
    daysUntilWeekend = 6 - dayOfWeek;
  }

  const weekend = new Date(today);
  weekend.setDate(today.getDate() + daysUntilWeekend);

  const year = weekend.getFullYear();
  const month = weekend.getMonth() + 1;
  const day = weekend.getDate();

  const formattedMonth = month < 10 ? `0${month}` : month.toString();
  const formattedDay = day < 10 ? `0${day}` : day.toString();

  return `${year}${formattedMonth}${formattedDay}`;
};