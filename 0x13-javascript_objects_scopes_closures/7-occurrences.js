#!/usr/bin/node
exports.nbOccurances = function (list, searchElement) {
	return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
