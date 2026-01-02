package WebSocket.websocket;
import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.simp.config.MessageBrokerRegistry;
import org.springframework.web.socket.config.annotation.EnableWebSocketMessageBroker;
import org.springframework.web.socket.config.annotation.StompEndpointRegistry;
import org.springframework.web.socket.config.annotation.WebSocketMessageBrokerConfigurer;

@Configuration
@EnableWebSocketMessageBroker // STOMP 동작 어노테이션
public class StompConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        // 클라이언트 → 서버 메시지 prefix
        // /app 으로 시작하는 메시지는 @MessageMapping이 처리
        config.setApplicationDestinationPrefixes("/app");

        // 서버 → 클라이언트 메시지 prefix (메시지 브로커가 관리)
        // /topic: 1:N 브로드캐스트 (게임방, 채팅방)
        // /queue: 1:1 개인 메시지
        config.enableSimpleBroker("/topic", "/queue");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        // 서버 엔드포인트와 클라이언트 엔드포인트가 반드시 동일해야 한다. (/endPointTest)
        // registry.addEndpoint("/endPointTest");                    // websocket

        // .withSockJS() : WebSocket 불가 시 대안 사용 (long polling, HTTP Streaming 등)
        registry.addEndpoint("/endPointTest").withSockJS();       // sockjs
    }

}