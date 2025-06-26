export const ssr = false;
import { getUsers } from '$lib/api/auth';
import { getSaveArticleList, getPublishingArticleList } from '$lib/api/docs/index.js';

export const load = async () => {
	let saveTotal = 0;
	let publishingTotal = 0;
	let userTotal = 0;
	try {
		const saveResponse = await getSaveArticleList(1, 1);
		saveTotal = saveResponse.data.content.total;
		const publishingResponse = await getPublishingArticleList(1, 1);
		publishingTotal = publishingResponse.data.content.total;
		const userResponse = await getUsers(1, 1);
		userTotal = userResponse.data.content.total;
	} catch (error) {
		console.error(error);
	}

	return {
		saveTotal,
		publishingTotal,
		userTotal
	};
};
