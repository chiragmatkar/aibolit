public class ExternalMethodCalls {

    private final String variable;

    NoExternalMethodCalls(final String value) {
        this.variable = value;
    }

    public String value() {
        return this.variable;
    }

    public char first() {
        return this.variable.charAt(0);
    }

    public char second() {
        return this.variable.charAt(1);
    }
}