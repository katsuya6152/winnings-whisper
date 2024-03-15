export const getWeekendDate = (): string => {
  const today = new Date();
  const dayOfWeek = today.getDay();
  const currentHour = today.getHours();

  let daysUntilWeekend: number;

  switch (dayOfWeek) {
    case 0:
      daysUntilWeekend = 0;
      break;
      case 6:
      if (currentHour >= 20) {
        // 現在時刻が20時以降であれば、日曜日のデータを取得
        daysUntilWeekend = 1;
      } else {
        daysUntilWeekend = 0;
      }
      break;
    default:
      daysUntilWeekend = 6 - dayOfWeek;
      break;
  }

  const weekend = new Date(today);
  weekend.setDate(today.getDate() + daysUntilWeekend);

  const year = weekend.getFullYear();
  const month = weekend.getMonth() + 1;
  const day = weekend.getDate();

  const formattedMonth = month.toString().padStart(2, '0');
  const formattedDay = day.toString().padStart(2, '0');

  return `${year}${formattedMonth}${formattedDay}`;
};