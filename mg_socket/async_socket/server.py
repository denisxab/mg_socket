from norm_import import iimport

from transport_levl import ServerIpAsync

host, port = iimport(__file__, 1, 'general_settings').From('host', 'port')
general_settings = iimport(__file__, 1, 'general_settings').module


# ImportError: attempted relative import with no known parent package
# ModuleNotFoundError: No module named 'server_transport'
# ImportError: cannot import name 'ServerIpAsync' from 'transport_level'
async def echo_server(message: str) -> str:
    return message


async def ack(message: str) -> str:
    return 'ok'


if __name__ == '__main__':
    # https://docs.python.org/3/library/asyncio-stream.html
    ServerIpAsync(
        host=host,
        port=port
    ).run(
        client_connected_cb=ServerIpAsync.base_handle,
        callback_build_send_data=ack
    )
