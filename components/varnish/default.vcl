vcl 4.0;
backend test {
  .host = "{{component.haproxy.connect.host}}";
  .port = "{{component.haproxy.connect.port}}";
}