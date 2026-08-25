from client import RealtimeScreenStreamVideoLatentDiffuserClient

def main():
    client = RealtimeScreenStreamVideoLatentDiffuserClient()
    res = client.stream_screen_latent_generation('WEBCAM_LIVE_FEED', 60, 'Photorealistic oil painting portrait')
    print('Stream Session: ' + res['stream_session_id'] + ' (Latency: ' + str(res['latent_diffusion_latency_ms']) + 'ms @ ' + str(res['fps']) + ' FPS)')
    print('Resolution: ' + res['spatial_resolution'] + ' | Frame Stability: ' + str(res['zero_drop_frame_rate_pct']) + '%')
    print('WebRTC URL: ' + res['webrtc_stream_url'])

if __name__ == '__main__':
    main()
