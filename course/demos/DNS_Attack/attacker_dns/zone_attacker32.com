$TTL 3D ; 3 days - tells DNS resolvers how long to cache the records before querying again for updates.
; SOA - Start of Authority - admin@attacker32.com is the email address of the person responsible for the domain
; ns.attacker32.com is the primary nameserver for the domain
@       IN      SOA   ns.attacker32.com. admin.attacker32.com. (
                2024100501  ; Serial number - increases whenever you make changes
                8H          ; 8 hours - Refresh - tells secondary DNS how often to check for changes 
                2H          ; 2 hours - Retry -tells secondary DNS how often to retry if the primary DNS is not reachable
                4W          ; 4 weeks - Expire - tells secondary DNS how long to keep the zone data if it can't contact the primary DNS
                1D)         ; 1 day - Minimum TTL - tells secondary DNS how long to keep the zone data in cache

@       IN      NS    ns.attacker32.com.   ; nameserver

@       IN      A     192.168.0.101        ; for attacker32.com
www     IN      A     192.168.0.101        ; for www.attacker32.com
abc     IN      A     192.168.0.102        ; for abc.attacker32.com
ns      IN      A     10.9.0.153           ; for ns.attacker32.com
*       IN      A     192.168.0.100        ; for other names
