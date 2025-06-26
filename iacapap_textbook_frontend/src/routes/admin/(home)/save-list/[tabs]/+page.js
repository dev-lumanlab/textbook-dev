export const ssr = false;
import { getSaveArticleList, searchSaveArticles } from '$lib/api/docs/index.js';

export const load = async ({ url, params }) => {
	const page = url.searchParams.get('page') || 1;
	const limit = params.tabs === 'list' ? 11 : 6;
	const search = url.searchParams.get('search') || '';

	let contents = [];
	let total = 0;
	try {
		let response;
		if (search) {
			response = await searchSaveArticles(search, page, limit);
		} else {
			response = await getSaveArticleList(page, limit);
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
