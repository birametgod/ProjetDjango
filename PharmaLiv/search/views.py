from django.shortcuts import render

# Create your views here.

def home(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['date', 'proposal','experiment_id','name_proposer'])

        found_entries = Experiment.objects.filter(entry_query)

    return render_to_response('data/home.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))
