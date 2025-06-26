import { getSaveArticle } from '$lib/api/docs/index.js';

export const ssr = false;

export const load = async ({ params }) => {
	const { id } = params;
	let content;
	try {
		const response = await getSaveArticle(id);
		content = response.data.content.article;
	} catch (error) {
		content = null;
		console.error(error);
	}

	return { content };
};
