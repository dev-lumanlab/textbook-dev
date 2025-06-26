export const ssr = false;
import { getPublishingArticleList, searchPublishedArticles } from '$lib/api/docs/index.js';

export const load = async ({ url, params }) => {
	const page = url.searchParams.get('page') || 1;
	const search = url.searchParams.get('search') || '';
	const limit = params.tabs === 'list' ? 11 : 6;

	let contents = [];
	let total = 0;
	try {
		let response;
		if (search) {
			response = await searchPublishedArticles(search, page, limit);
		} else {
			response = await getPublishingArticleList(page, limit);
		}
		contents = response.data.content.articles;
		total = response.data.content.total;
	} catch (error) {
		console.error(error);
	}

	return {
		contents,
		total,
		limit
	};
};
