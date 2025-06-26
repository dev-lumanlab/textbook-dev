import dayjs from 'dayjs';

export const dateFormat = (date) => {
	return dayjs(date).format('YYYY. MM. DD HH:mm');
};

export const dateTimeFormat = (date) => {
	return dayjs(date).format('YYYY. MM. DD HH:mm:ss');
};
