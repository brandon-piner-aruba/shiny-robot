import dns.name
import dns.message
import dns.query
import dns.flags
import time
import statistics


def dns_time(domain='stackoverflow.com'):
    name_server = '8.8.8.8'
    ADDITIONAL_RDCLASS = 65535
    domain = dns.name.from_text(domain)
    if not domain.is_absolute():
        domain = domain.concatenate(dns.name.root)

    request = dns.message.make_query(domain, dns.rdatatype.ANY)
    request.flags |= dns.flags.AD
    request.find_rrset(request.additional, dns.name.root, ADDITIONAL_RDCLASS,
                       dns.rdatatype.OPT, create=True, force_unique=True)
    dns_times = []
    for a in range(20):
        dns_start = time.time()
        response = dns.query.udp(request, name_server)
        dns_end = time.time()
        dns_time = (dns_end - dns_start) * 1000
        dns_times.append(dns_time)
    dns_mean = statistics.mean(dns_times)

    return 'DNS time            = %.2f ms' % (dns_mean)
