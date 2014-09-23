all:	CHANGES

CHANGES:	
	git log --oneline --pretty=formay:"%ad: %s" --date=short > CHANGES

