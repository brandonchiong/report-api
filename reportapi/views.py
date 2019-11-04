from django.http import JsonResponse, HttpResponseBadRequest
from .models import Report
import json


def create(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            report = Report()
            report.title = json_data['title']
            report.description = json_data['description']
            report.created_by = json_data['created_by']

        except KeyError:
            return HttpResponseBadRequest('Body must have "title", "description", and "created_by" fields.')

        report.save()

        response = {
            'content': 'Report ID: ' + str(report.id)
        }

        return JsonResponse(response)
    else:
        return HttpResponseBadRequest('POST method required.')


def read(request, report_id):
    report = Report.objects.get(id=report_id)

    response = {
        'title': report.title,
        'description': report.description,
        'created_by': report.created_by,
        'created_at_timestamp': int(report.created_at.timestamp())
    }

    return JsonResponse(response)


def update(request, report_id):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        report = Report.objects.get(id=report_id)

        if 'title' in json_data:
            report.title = json_data['title']
        if 'description' in json_data:
            report.description = json_data['description']
        if 'created_by' in json_data:
            report.created_by = json_data['created_by']

        report.save()

        response = {
            'title': report.title,
            'description': report.description,
            'created_by': report.created_by,
            'created_at_timestamp': int(report.created_at.timestamp())
        }

        return JsonResponse(response)
    else:
        return HttpResponseBadRequest('POST method required.')


def delete(request, report_id):
    report = Report.objects.get(id=report_id)
    report.delete()

    response = {
        'content': 'Report deleted successfully.'
    }

    return JsonResponse(response)


def all_reports(request):
    reports = Report.objects.values()
    response = {}

    for report in reports:
        response[report['id']] = report['title']

    return JsonResponse(response)

