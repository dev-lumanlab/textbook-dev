import { getSaveArticle } from '$lib/api/docs';

export const ssr = false;

export const load = async ({ params }) => {
	const { id } = params;
	const response = await getSaveArticle(id);
	const article = response.data.content.article;

	return {
		article
	};
};
