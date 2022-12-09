from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from User.models import BlockedIP
from django.shortcuts import render
class BlockIpMiddleware(MiddlewareMixin):
    def process_request(self, request):
        blocked_ips = BlockedIP.objects.all()
        blocked_ips_list= [ip.ip_addr for ip in blocked_ips]
        print(blocked_ips_list)
        if request.META['REMOTE_ADDR'] in blocked_ips_list:
            return render(request, 'forbidden.html')
        print(request.META['REMOTE_ADDR'])


