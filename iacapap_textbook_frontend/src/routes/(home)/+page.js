export const ssr = false;
import { getPublishingArticleList, getSaveArticle } from '$lib/api/docs';

export const load = async () => {
	let contents = [];
	try {
		const response = await getPublishingArticleList(1, 10);
		const articleIdList = response.data.content.articles.map((article) => article.id);

		for (const articleId of articleIdList) {
			try {
				const response = await getSaveArticle(articleId);
				const article = response.data.content.article;
				contents = [...contents, article];
			} catch (error) {
				console.error(error);
			}
		}
	} catch (error) {
		console.error(error);
	}

	return {
		contents
	};
};
