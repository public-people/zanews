import re

from django.contrib.postgres.search import SearchQuery, SearchVector
from rest_framework.filters import BaseFilterBackend
from django import forms
from django.utils.safestring import mark_safe


PHRASE_RE = re.compile(r'"([^"]*)("|$)')


class FullTextSearchFilter(BaseFilterBackend):
    """
    Filter on phrase provided by
    """

    def filter_queryset(self, request, queryset, view):

        query = request.query_params.get("basic_web_search", None)

        if query:

            phrases = [p[0].strip() for p in PHRASE_RE.findall(query)]
            phrases = [p for p in phrases if p]
            terms = PHRASE_RE.sub("", query).strip()

            if terms:
                compound_statement = SearchQuery(terms)

            if phrases:
                if terms:
                    compound_statement = compound_statement & SearchQuery(
                        phrases[0], search_type="phrase"
                    )
                else:
                    compound_statement = SearchQuery(phrases[0], search_type="phrase")

                for phrase in phrases[1:]:
                    compound_statement = compound_statement & SearchQuery(
                        phrase, search_type="phrase"
                    )
            if terms or phrases:
                print(compound_statement)

                queryset = queryset.filter(full_text_search=compound_statement)

        return queryset

    def to_html(self, request, queryset, view):
        fields = FullTextSearchForm().as_p()
        return mark_safe(f'<form action="" method="get">{ fields }</form>')


class FullTextSearchForm(forms.Form):
    basic_web_search = forms.CharField(label='Search query')
